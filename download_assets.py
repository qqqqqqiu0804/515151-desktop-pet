import urllib.request
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
os.makedirs(assets_dir, exist_ok=True)

images = [
    ('https://aka.doubaocdn.com/s/PMZA1wnxSY', 'cat_stand.jpg'),
    ('https://aka.doubaocdn.com/s/yGHO1wnxSa', 'cat_sit.jpg'),
    ('https://aka.doubaocdn.com/s/Ymnl1wnxSd', 'cat_lie.jpg'),
]

for url, filename in images:
    path = os.path.join(assets_dir, filename)
    print(f'Downloading {filename}...')
    urllib.request.urlretrieve(url, path)
    print(f'Saved to {path}')

print('All images downloaded.')
