import setuptools

print(setuptools.find_packages())

setuptools.setup(name='pdfviewer',
                 version='0.1',
                 description='Tkinter based GUI to view PDF files',
                 author='rizalachp',
                 author_email='rizal.ahmadp@gmail.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 install_requires=[
                     'Pillow',
                     'pdfplumber',
                     'PyPDF2',
                     'pytesseract'
                 ],
                 zip_safe=False)
