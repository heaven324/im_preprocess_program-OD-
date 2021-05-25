## My image labelling(bbox) program

# object
1. 범용 프로그램을 쓰기보다 내 상황과 목적에 맞게 코드라인부터 수정할 수 있는 프로그램 구성
2. 직접 gui 프로그램을 만들면서 gui에대한 공부와 내 코드를 배포가능한 프로그램으로 구성하는 방법 공부



## 오늘 진행상황(버전관리용)

opencv의 편집툴과 gui를 연동하기 위해서 이미지 렌더링 방식을 변경해서 적용

cv_func파일을 만들고 이미지 로드함수 추가(앞으로의 opencv작업을 따로 구분하기 위해서)

위젯 위치와 크기 재배열

창 크기 변경 후 고정

찾아본건 많은데 실제로 코드를 만든건 별로 없네 ㅠ



## 버그 리포트

1. 이미지 파일을 클릭해서 라벨 위젯에 이미지를 띄울 때 너무 빨리 빨리 여러 이미지를 클릭하면 이미지가 안뜸
2. 트리에서 경로 선택 후 이미지 클릭시 이미지 안 뜸(fname 변수가 변하는 이벤트가 없기 때문) [내일 만들자]



# 생각 정리

2 우선은 gui를 이미지를 띄워주는 단계까지 완성하고 편집 프로그램 구성을 해야겠다



1 코드라인까지 익히면서 공부하는 것 보다는 QtDesigner프로그램으로 포맷을 만들고 이미지 편집 툴을 구성하는 것이 더 좋을 것 같다 지금 까지 QtDesigner툴을 봐온 바로는 qt5패키지 만으로는 이미지 편집툴을 구성할 수 없다 그러니 openCV의 이미지 처리를 하나의 편집 툴로 만들어서 gui위에 올리는 방식으로 만들어야 할것 같다 

전체 구성안에 대해서 생각한 것들을 정리하자면 gui 구성에서 왼쪽에 디렉토리 하나를 불러와서 그안의 모든 이미지 파일을 열방향으로 나열해서 표시해주고 그 중 편집할 이미지를 클릭하면 화면 오른쪽에 표시가 되며 화면 오른쪽에서 편집이 진행되는 방식.   편집 방식으로는 첫 로드에 이미지 전체가 보일 수 있게 resize장치를 마련하고 우클릭 드래그로 표시한 이미지 확대, 우클릭으로 화면 축소, 좌클릭 드래그로 true ancher box 그리기, 엔터버튼으로 왼쪽에 열려있는 디렉토리에 ancher좌표를 xml로 저장(파일명은 이미지파일명과 같게)

오늘은 여기까지