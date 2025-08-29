#pip install nbformat로 먼저 nbformat 패키지를 설치하세요.
import nbformat

# 두 개 노트북 로드
# ipynb_merging.py와 동일한 디렉토리에 두 파일이 있어야 합니다.
# 동일한 파일이 없다면 경로를 입력하세요. 예: "path/to/your/notebook.ipynb"
nb1 = nbformat.read("supercoding_project1.ipynb", as_version=4)
nb2 = nbformat.read("dd_0826.ipynb", as_version=4)

# nb1의 셀 뒤에 nb2의 셀 추가
nb1.cells.extend(nb2.cells)

# 새로운 파일로 저장
with open("Semi_Final_Code.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb1, f)