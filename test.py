from zeroth_normalizer import ZerothKoreanNormalizer

dataset = [
  '대왕 대비가 대행왕이 예(睿)로써 시호를 삼도록 말했었다고 알리다',
  '한국어 위키백과(영어: Korean Wikipedia)는 한국어로 운영되는 위키백과의 다언어판 가운데 하나로서, 2002년 10월 11일에 시작되었다. ',
  "공식 문서에는 'Corea' 또는 'Korea'가 혼용되어 사용되었고, 1900년대 초기부터 영어권에서는 'Korea'의 사용 빈도가 높았다. ",
  "  북위 33도~38도, 동경 126~132도에 걸쳐 있어 냉대 동계 소우 기후와 온대 하우 기후, 온난 습윤 기후가 나타난다.",
  "3.1운동",
  "평균 기온은 10 ~ 16℃이며, 가장 무더운 달인 8월은 23 ~ 36℃, 5월은 16 ~ 19℃, 10월은 11 ~ 19℃, 가장 추운 달인 1월은 -6 ~ 3℃이다.",
  "예시로서, 만약 크기 n의 모든 입력에 대한 알고리즘에 필요한 시간이 최대 (어떤 n0보다 크지 않은 모든 n에 대하여) 5n^3 + 3n의 식을 가진다면, 이 알고리즘의 점근적 시간 복잡도는 O(n3)이라고 할 수 있다.",
]

normalizer = ZerothKoreanNormalizer()

for data in dataset:
  print('원문:\t', data)
  print('step1:\t', normalizer(data, steps=1))
  print('step2:\t', normalizer(data, steps=2))
  print('step3:\t', normalizer(data, steps=3))
  print('step4:\t', normalizer(data, steps=4))
  print()