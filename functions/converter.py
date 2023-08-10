import aspose.words as aw
import io

def convertion(inputExt, outputExt, filePath, fileName):
    converted = aw.Document(filePath)
    savePath = f"./assets/{fileName}.{outputExt}"

    converted.save(savePath)
    return savePath

