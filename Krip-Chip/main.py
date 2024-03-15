import base64
import os
from flet import *
from lib.modifiedRC4 import rc4
import random

# Global variables

inputType = "text"
fileDir = None
result = None
originalFileName = None

async def main(page: Page):    
    global inputType, result, fileDir, originalFileName
    page.title = "Krip-Chip"
    page.theme = Theme(
        color_scheme_seed=colors.CYAN,
    )

    # Button handlers

    async def randomizeKey(e):
        key = "".join([chr(random.randint(33, 126)) for _ in range(64)])
        print(key)
        inputKey.value = key
        page.update()

    async def dialogPicker(e: FilePickerResultEvent):
        global fileDir
        selectedFile.visible = True
        fileDir = e.files[0].path
        selectedFile.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selectedFile.update()

    async def handleChange(e):
        global inputType
        inputType = e.data[2:-2]
        print(inputType)
        if inputType == "text":
            fileInput.visible = False
            plainText.visible = True
        else:
            fileInput.visible = True
            selectedFile.visible = False
            plainText.visible = False
        page.update()

    async def copyResult(e):
        text = resultText.value
        page.set_clipboard(text)
        page.update()

    async def saveResult(e):
        global result, mode, originalFileName
        print("Saving...")
        saveLocation = e.path
        print(result)
        if saveLocation:
            try:
                if originalFileName == None:
                    with open(os.path.join(saveLocation, "Kripik.hts"), "wb") as f:
                        f.write(result)
                    f.close()
                else:
                    with open(os.path.join(saveLocation, originalFileName), "wb") as f:
                        f.write(result)
                    f.close()
            except Exception as e:
                print(e)
        page.update()

    async def encrypt(e):
        global inputType, result, fileDir, originalFileName
        key = inputKey.value
        print("Encrypting...")
        if key != "":
            if inputType == "text":
                # Encrypt
                plaintext = plainText.value
                cp = rc4(key)
                ciphertext = cp.encrypt(plaintext.encode())
                result = cp.encrypt(("text.txt|" + plaintext).encode())
                print(''.join([chr(i) for i in ciphertext]))
                resultText.value = base64.b64encode(ciphertext).decode()
            else:
                # get file dir
                print("fileDir:", fileDir)
                file = open(fileDir, "rb")
                fileContent = file.read()
                file.close()
                if "/" in fileDir:
                    originalFileName = fileDir.split('/')[-1]
                else:
                    originalFileName = fileDir.split('\\')[-1]
                # Concatenate original file name with file content in bytes
                fileContent = ''.join([chr(i) for i in fileContent])
                fileContent = originalFileName + '|' + fileContent

                print(fileContent)

                cp = rc4(key)
                ciphertext = cp.encrypt(fileContent.encode())
                result = ciphertext
                resultText.value = base64.b64encode(ciphertext).decode()
                originalFileName = None

            resultContainer.visible = True
            
        page.update()
        ...

    async def decrypt(e):
        global inputType, result, fileDir, originalFileName
        key = inputKey.value
        print("Decrypting...")
        if key != "":
            if inputType == "text":
                # Decrypt
                ciphertext = base64.b64decode(plainText.value)
                cp = rc4(key)
                plaintext = cp.decrypt(ciphertext).decode()
                resultText.value = plaintext
            else:
                #get file dir
                print("fileDir:", fileDir)
                file = open(fileDir, "rb")
                fileContent = file.read()
                print(fileContent)
                file.close()
                
                cp = rc4(key)
                plaintext = cp.decrypt(fileContent)
                plaintext = ''.join([chr(i) for i in plaintext])
                originalFileName = plaintext.split('|')[0]
                result = plaintext.split('|')[1].encode()
                resultText.value = plaintext.split('|')[1]
                

            resultContainer.visible = True
        page.update()
        ...

    # App components
        
    pickFile = FilePicker(on_result=dialogPicker)
    saveFile = FilePicker(on_result=saveResult)
    page.overlay.append(pickFile)
    page.overlay.append(saveFile)

    selectedFile = Text()

    plainText = TextField(
        label="Plaintext",
        multiline=True,
        min_lines=5,
        max_lines=5,
        border_radius=20,
    )

    inputKey = TextField(
        label="Key",
        border_radius=20,
        expand=4
    )

    resultText = TextField(
        label="Result",
        multiline=True,
        min_lines=5,
        max_lines=5,
        border_radius=20,
        read_only=True,
    )

    fileInput = Container(
        content=Column(
            [
                ElevatedButton(
                    "Upload File",
                    on_click=lambda _: pickFile.pick_files(),
                ),
                Text("Usahakan file < 1KB"),
                selectedFile,
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        padding=padding.symmetric(vertical=50),
        alignment=alignment.center,
        width=1000,
        border=border.all(1, colors.ON_SURFACE_VARIANT),
        border_radius=20,
    )
    fileInput.visible = False

    resultButton = Row(
        [
            FilledButton(
                text="Save",
                on_click=lambda _: saveFile.get_directory_path(),
                style=ButtonStyle(
                    padding=15,
                ),
                expand=True,
            ),
            OutlinedButton(
                text="Copy",
                on_click=copyResult,
                style=ButtonStyle(
                    padding=15,
                ),
                expand=True,
            ),
        ]
    )

    resultContainer = Container(
        content=Column(
            [
                resultText,
                resultButton,
            ],
            spacing=10,
            wrap=False,
        ),
    )
    resultContainer.visible = False


    page.add(
        SafeArea(
            Container(
                width="100%",
                height="100%",
                padding=20,
                content=Column(
                    [
                        SegmentedButton(
                            on_change=handleChange,
                            show_selected_icon=False,
                            selected={"text"},
                            segments=[
                                Segment(
                                    value="text",
                                    label=Text("Text"),
                                ),
                                Segment(
                                    value="file",
                                    label=Text("File"),
                                ),
                            ]
                        ),
                        Column(
                            [
                                plainText,
                                fileInput,
                                Row(
                                    [
                                        inputKey,
                                        Container(
                                            content=IconButton
                                            (
                                                icon=icons.REFRESH,
                                                on_click=randomizeKey,
                                            ),
                                            bgcolor=colors.CYAN_50,
                                            border_radius=20,
                                        ),
                                    ],
                                ),
                                Row(
                                    [
                                        FilledButton(
                                            text="Encrypt",
                                            on_click=encrypt,
                                            style=ButtonStyle(
                                                padding=15,
                                            ),
                                            expand=True,
                                        ),
                                        OutlinedButton(
                                            text="Decrypt",
                                            on_click=decrypt,
                                            style=ButtonStyle(
                                                padding=15,
                                            ),
                                            expand=True,
                                        ),
                                    ]
                                ),
                            ],
                            spacing=10,
                        ),
                        resultContainer,
                    ],
                    spacing=25,
                    alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            ),
            expand=True,
        )
    )

if __name__ == "__main__":
    app(main)
