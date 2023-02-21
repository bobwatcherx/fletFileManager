from flet import *
import os
import shutil
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
            ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
            ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
            ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
    }
def get_file_format(file_name):
        return os.path.splitext(file_name)[1].lower()

def get_directory(file_format):
    for directory, file_formats in DIRECTORIES.items():
        if file_format in file_formats:
            return directory
    return None

def organize_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_format = get_file_format(file_name)
            directory = get_directory(file_format)
            if directory is None:
                continue
            source_path = os.path.join(root, file_name)
            destination_dir = os.path.join(os.getcwd(), directory)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.copy(source_path, destination_path)
            print("COPY .... ",source_path)
    print("SUDAH SEELSAI------")


organize_files("/home")

    


def main(page:Page):
    page.scroll = "auto"

    myarchive = Column(scroll="always")
    mydocuments = Column(scroll="always")
    myaudio = Column(scroll="always")
    myhtml = Column(scroll="always")
    myimages = Column(scroll="always")
    myplaintext = Column(scroll="always")
    mypdf = Column(scroll="always")
    myvideos = Column(scroll="always")
    mypython = Column(scroll="always")
    myxml = Column(scroll="always")
    myexe = Column(scroll="always")
    myshell = Column(scroll="always")

    

    

    mytab = Tabs(
            selected_index=1,
            animation_duration=200,
            tabs=[
                Tab(
                text="Archives",
                content=myarchive
                ),
                Tab(
                text="Document",
                content=mydocuments
                ),
                Tab(
                text="Audio",
                content=myaudio
                ),
                Tab(
                text="Html",
                content=myhtml
                ),
                Tab(
                text="Images",
                content=myimages
                ),
                Tab(
                text="PainText",
                content=myplaintext
                ),
                Tab(
                text="PDF",
                content=mypdf
                ),
                Tab(
                text="Videos",
                content=myvideos
                ),
                Tab(
                text="Python",
                content=mypython
                ),
                Tab(
                text="XML",
                content=myxml
                ),
                Tab(
                text="EXE",
                content=myexe
                ),
                Tab(
                text="SHELL",
                content=myshell
                ),

            ],
            expand=1
        )
    folders = ['HTML', 'IMAGES', 'VIDEOS', 'DOCUMENTS', 'ARCHIVES', 'AUDIO', 'PLAINTEXT', 'PDF', 'PYTHON','XML','EXE','SHELL']

    for folder in folders:
        folder_path = folder
        file_list = []

        try:
            file_list = os.listdir(folder_path)
        except FileNotFoundError:
            print(f"Folder tidak ditemukan: {folder_path}")
            continue

        if folder == 'ARCHIVES':
            for file_name in file_list:
                myarchive.controls.append(ListTile(leading=Icon(name="article"), title=Text(file_name)))
        elif folder == 'IMAGES':
            for file_name in file_list:
                myimages.controls.append(ListTile(leading=Icon(name="description"), title=Text(file_name)))
        elif folder == 'VIDEOS':
            for file_name in file_list:
                myvideos.controls.append(ListTile(leading=Icon(name="movie"), title=Text(file_name)))
        elif folder == 'DOCUMENTS':
            for file_name in file_list:
                mydocs.controls.append(ListTile(leading=Icon(name="description"), title=Text(file_name)))
        elif folder == 'AUDIO':
            for file_name in file_list:
                myaudio.controls.append(ListTile(leading=Icon(name="music_note"), title=Text(file_name)))
        elif folder == 'PLAINTEXT':
            for file_name in file_list:
                myplaintext.controls.append(ListTile(leading=Icon(name="description"), title=Text(file_name)))
        elif folder == 'PDF':
            for file_name in file_list:
                mypdf.controls.append(ListTile(leading=Icon(name="picture_as_pdf"), title=Text(file_name)))
        elif folder == 'PYTHON':
            for file_name in file_list:
                mypython.controls.append(ListTile(leading=Icon(name="description"), title=Text(file_name)))
        elif folder == 'XML':
            for file_name in file_list:
                myxml.controls.append(ListTile(leading=Icon(name="description"), title=Text(file_name)))
        elif folder == 'EXE':
            for file_name in file_list:
                myexe.controls.append(ListTile(leading=Icon(name="slideshow"), title=Text(file_name)))
        elif folder == 'SHELL':
            for file_name in file_list:
                myshell.controls.append(ListTile(leading=Icon(name="terminal"), title=Text(file_name)))
        elif folder == 'HTML':
            for file_name in file_list:
                myhtml.controls.append(ListTile(leading=Icon(name="description"), title=Text(file_name)))



    page.add(
        AppBar(
        title=Text("File manager App",color="white",size=30,weight="bold"),
        bgcolor="blue"        
        ),
        Column([
        mytab
        ])

    )
flet.app(target=main)


