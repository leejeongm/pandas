import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import FuncFormatter

# 나눔바른펜 폰트 경로 설정
font_location = r"C:\Windows\Fonts\NanumBarunpenR.ttf"

# 폰트 설정
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

# Excel 파일에서 데이터 읽기
excel_file_path = r"C:\Users\hyoun\Downloads\내국인(블록) 일자별시간대별.xlsx"  # 실제 파일 경로 및 이름으로 변경
df = pd.read_excel(excel_file_path)

# 요일을 정렬 (월요일부터 일요일까지)
days_order = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
df['요일(DAW)'] = pd.Categorical(df['요일(DAW)'], categories=days_order, ordered=True)
df = df.sort_values('요일(DAW)')

# 데이터 확인
print(df)

# 막대형 차트 생성
colors = {'월요일': 'skyblue', '화요일': 'lightgreen', '수요일': 'lightcoral', '목요일': 'gold', 
          '금요일': 'orange', '토요일': 'lightpink', '일요일': 'lightskyblue'}

fig, ax = plt.subplots()

for day, color in colors.items():
    day_data = df[df['요일(DAW)'] == day]
    ax.bar(day_data['요일(DAW)'], day_data['카드이용금액계(AMT_CORR)'], color=color, label=day)

# 차트 제목 및 레이블 추가
plt.title('요일별 신용카드 매출 분석')
plt.xlabel('요일')
plt.ylabel('매출액')

# 범례 추가
ax.legend()

# y 축 포맷팅 함수 정의 (금액 형식으로 변환)
def format_currency(value, tick_number):
    return '{:,.0f}'.format(value)

# y 축 포맷팅 함수 적용
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_currency))

# 차트 표시
plt.show()