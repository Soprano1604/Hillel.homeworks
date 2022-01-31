from PIL import Image

print('Hey! Here we have such a big image: 6240x4160. \nIt would be nice to decrease it, right?')
new_width = int(input('Set new image width: '))
new_height = int(input('Set new image height: '))


def resize_images(input_image_path, output_image_path, size):
    big_image = Image.open(input_image_path)
    resized_image = big_image.resize(size)
    width, height = resized_image.size
    print(f'Great!\nNew image size is much better: ', width, 'x', height)
    resized_image.show()
    resized_image.save(output_image_path)

if __name__ == '__main__':
    resize_images(input_image_path='test.jpg',
                 output_image_path='test_resized.jpg',
                 size=(new_width, new_height))
