from rembg import remove
from PIL import Image
import easygui as eg


print("Start ...")
input_path = eg.fileopenbox(title="Selectionné un fichier image")
output_path = eg.filesavebox(title="Save file to...")
inputImg = Image.open(input_path)
output = remove(inputImg)
output.save(output_path)
print("End ...")
