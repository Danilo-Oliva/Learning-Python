import torch
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

#creando un tensor
arreglo = [[2, 3, 4], [1, 5, 6]]
tensor1 = torch.tensor(arreglo)

#en donde está conectado
tensor1.device

#ver si se está usando la gpu o la cpu
device = (
  "cuda" if torch.cuda.is_available()
  else "cpu"
)

#cambiar a GPU o cpu
#tensor1 = tensor1.to("cuda")
#tensor1 = tensor1.to("cpu")

#saber el tamaño del tensor
tensor1.shape

data_mnist = datasets.MNIST(
  root= "datos", #carpeta donde almaceno el dataset
  train=True,
  download=True,
  transform=ToTensor()
)

figure = plt.figure(figsize=(8, 8))
fils, cols = 3, 3
for i in range(1, cols * fils + 1):
  #Escoger una imagen aleatoria
  sample_idx = torch.randint(len(data_mnist), size=(1,)).item()
  
  #extraer imagen y categoria
  img, label = data_mnist[sample_idx]
  
  #dibujar
  figure.add_subplot(fils, cols, i)
  plt.title(str(label))#categoria
  plt.axis("off")
  plt.imshow(img.squeeze(), cmap="gray") #imagen
plt.show()
