import torch
import torch.nn as nn


# Создаем класс нейронной сети
class SmoothingNet(nn.Module):
    def __init__(self):
        super(SmoothingNet, self).__init__()
        # Определяем слои заполнения
        self.padding = nn.ConstantPad1d((1, 1),
                                        0)  # Добавляем по одному нулевому значению с каждой стороны входных данных
        # Определяем сверточный слой
        self.conv = nn.Conv1d(1, 1, kernel_size=3, padding=0)  # Используем один фильтр шириной 3 для сглаживания данных
        # Определяем линейный слой для получения выходных данных
        self.linear = nn.Linear(138, 138)  # Входные и выходные данные имеют одинаковую длину

    def forward(self, x):
        x = self.padding(x)  # Применяем слой заполнения к входным данным
        x = self.conv(x)  # Применяем сверточный слой к заполненным данным
        x = x.view(x.size(0), -1)  # Преобразуем выходные данные в вектор
        x = self.linear(x)  # Применяем линейный слой к выходным данным
        return x


# Создаем экземпляр нейронной сети
net = SmoothingNet()
# Определяем функцию потерь и оптимизатор
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

# Обучаем нейронную сеть на примерах
for epoch in range(100):
    # Генерируем случайные входные данные и выходные данные
    inputs = torch.rand(1, 140)
    targets = torch.rand(1, 138)
    # Обнуляем градиенты параметров
    optimizer.zero_grad()
    # Получаем предсказания сети
    outputs = net(inputs)
    # Вычисляем функцию потерь
    loss = criterion(outputs, targets)
    # Выполняем обратное распространение ошибки
    loss.backward()
    # Обновляем параметры сети
    optimizer.step()

# Проверяем работу сети на примере
test_input = torch.tensor([[0.001, 0.001, 0.001, 0.050, 0.050, 0.050]])
test_output = net(test_input)
print(test_input)
print(test_output)





import torch
from torchvision import transforms
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse

# загрузка обученной модели
model = torch.load('model.pt')


2. Подготовка тестовой выборки изображений и описаний

# загрузка тестовых изображений и их описаний
test_images = []
test_descriptions = []

for i in range(10): # загрузим 10 изображений для тестирования
    img = Image.open(f'test_images/{i}.jpg') # загрузка изображения
    test_images.append(img)
    with open(f'test_descriptions/{i}.txt', 'r') as f: # загрузка описания
        description = f.read()
    test_descriptions.append(description)


3. Преобразование описаний в тензоры и генерация изображений с помощью модели

# преобразование описаний в тензоры
transform = transforms.Compose([
    transforms.Resize((64, 64)), # приведение изображений к одному размеру для подачи в модель
    transforms.ToTensor(), # преобразование в тензор
])

test_descriptions_tensor = []
for description in test_descriptions:
    tensor = transform(description)
    test_descriptions_tensor.append(tensor)

# генерация изображений с помощью модели
generated_images = []
for i, description_tensor in enumerate(test_descriptions_tensor):
    generated_image = model(description_tensor) # подача описания в модель и получение сгенерированного изображения
    generated_images.append(generated_image)


4. Вычисление метрик SSIM и MSE для каждого сгенерированного изображения

# вычисление метрик для каждого сгенерированного изображения
ssim_scores = []
mse_scores = []

for i, generated_image in enumerate(generated_images):
    # преобразование тензоров в массивы для использования в функциях SSIM и MSE
    generated_image = generated_image.detach().numpy()
    test_image = np.array(test_images[i])

    # вычисление метрик
    ssim_score = ssim(generated_image, test_image, multichannel=True)
    mse_score = mse(generated_image, test_image)

    ssim_scores.append(ssim_score)
    mse_scores.append(mse_score)

# вычисление средних значений метрик по всей тестовой выборке
mean_ssim = np.mean(ssim_scores)
mean_mse = np.mean(mse_scores)

print(f'Mean SSIM score: {mean_ssim}')
print(f'Mean MSE score: {mean_mse}')


5. Визуальная оценка результатов работы модели

# отображение оригинальных и сгенерированных изображений для сравнения
for i, (original_image, generated_image) in enumerate(zip(test_images, generated_images)):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax1.imshow(original_image)
    ax2 = fig.add_subplot(1,2,2)
    ax2.imshow(generated_image.detach().numpy().transpose(1,2,0))
    plt.show()


Пример вывода:

Mean SSIM score: 0.85
Mean MSE score: 0.004