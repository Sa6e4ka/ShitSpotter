## В этом репозитории имеется чуть-чуть настроенное CI (Contibiuos integration): 
При каждом коммите будет происходить проверка правильности написания кода, также в папке test можно будет добавить код, для того чтобы каждый раз при коммите происходило тестировочное распознавание расознования объекта на фотографии sample.jpg.
Но это офк по желанию и надобности :) 

При устновке репозитория не забудь установить те зависимости которые есть в requirements.txt потому что для CI нужно установить

```bash
pip install pre-commit
pre-commit install 
```
Если вдруг не хочешь, что бы проходила обязательная проверка кода при каждом коммите, то можешь выполнить:

```bash
git commit -m "Пропускаю pre-commit" --no-verify
```
Это сможет одноразово (!) скипнуть проверку (просто без валидации чистот кода, он не даст закоммитить)

## 📂 Структура репозитория

/data                 # Датасеты (не загружается в Git)  
/notebooks            # Jupyter-ноутбуки для обучения и тестирования  
/models               # Сохраненные веса модели  
/src                  # Код: препроцессинг, обучение, инференс  
/tests                # Тесты для CI  
    │── train.py          # Скрипт для обучения  
    │── detect.py         # Скрипт для инференса  
    │── utils.py          # Вспомогательные функции  
/requirements.txt     # Зависимости проекта  
/.github/workflows    # Конфигурация CI/CD  
/.pre-commit-config.yaml # Автопроверки кода  

## 🔧 Установка и настройка

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/your-username/yolo-poop-detector.git
cd yolo-poop-detector
```

### 2️⃣ Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3️⃣ Настройка pre-commit (опционально)
Pre-commit автоматически форматирует код перед коммитами.
```bash
pre-commit install
```

## 📤 Работа с Git

### Как внести изменения?

1. Создайте новую ветку:

```bash
git checkout -b feature-new-function
```

2. Внесите изменения, добавьте их в коммит:

```bash
git add .
git commit -m "Добавил новую функцию"
```

3. Отправьте изменения в репозиторий:

```bash
git push origin feature-new-function
```

4. Создайте Pull Request в GitHub.

## 🚀 Автоматизация (CI/CD)

### Каждый коммит проверяется в GitHub Actions: формат кода, тесты.