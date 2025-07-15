from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch
from torch.utils.data import DataLoader, TensorDataset
from .relationship_training_data import train_texts, train_labels

class RelationshipDetector:
    def __init__(self):
        self.model_name = "roberta-base"
        self.tokenizer = RobertaTokenizer.from_pretrained(self.model_name)
        self.model = RobertaForSequenceClassification.from_pretrained(
            self.model_name,
            num_labels=6
        )
        
        self.relationships = {
            0: "parent-child",
            1: "romantic-partners",
            2: "friends",
            3: "siblings",
            4: "professional",
            5: "myself",
        }

    def train(self, train_texts: list, train_labels: list, epochs=3, batch_size=8):
        # Tokenize data
        encodings = self.tokenizer(
            train_texts, 
            truncation=True, 
            padding=True, 
            return_tensors="pt"
        )
        
        dataset = TensorDataset(
            encodings['input_ids'],
            encodings['attention_mask'],
            torch.tensor(train_labels)
        )
        
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=5e-5)
        
        self.model.train()
        for epoch in range(epochs):
            total_loss = 0
            for batch in dataloader:
                optimizer.zero_grad()
                input_ids, attention_mask, labels = batch
                outputs = self.model(input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
            print(f"Epoch {epoch+1}, Loss: {total_loss/len(dataloader):.4f}")
        
        torch.save(self.model.state_dict(), "relationship_model.pth")
        print("Training complete! Model saved to 'relationship_model.pth'.")

    def predict(self, texts: list) -> list:
        """Predict relationship class for a list of texts."""
        self.model.eval()
        
        encodings = self.tokenizer(
            texts,
            truncation=True,
            padding=True,
            return_tensors="pt"
        )
        
        with torch.no_grad():
            outputs = self.model(
                input_ids=encodings["input_ids"],
                attention_mask=encodings["attention_mask"]
            )
            predictions = torch.argmax(outputs.logits, dim=1)
        
        labels = [self.relationships[int(label)] for label in predictions]
        return labels
    

if __name__ == "__main__":
    detector = RelationshipDetector()
    detector.train(train_texts, train_labels, epochs=3)
