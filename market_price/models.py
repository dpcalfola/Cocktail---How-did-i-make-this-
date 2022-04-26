from django.db import models


class LiqueurPriceInformation(models.Model):
    """
    주종 (varchar 30 blank=True 위스키, 보드카, 럼...
    이름 (varchar 50 글렌피딕, 아드벡, 아마레또...
    라인업 (varchar 50, blank=True,  그린라벨, Signet, 나두라..
    숙성년도 (Integer blank=True, null=True(없을시 에러 발생) -> 12년...
    가격 (Integer -> ₩50,000...) -> 모델은 정수 타입. 데이터를 불러온 뒤에 ₩50,000 형태로 파싱
    용량 (Integer -> 700ml)
    구입 경로 (varchar 100)
    가격 확인 날짜 (Date)
    비고 (varchar 100)

    # 여기서부터는 DB 에만 저장
    작성일(DateTime)
    작성자(User) -> 외래키, 타입 방법 확인 요망
    """

    # blank and null rule
    # CharField -> blank=True
    # Integer -> blank=True, null=True

    category_1 = models.CharField(max_length=30, blank=True)
    category_2 = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=50)
    lineup = models.CharField(max_length=50, blank=True)
    aged = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    purchasing_route = models.CharField(max_length=100)
    confirmation_date = models.DateField()
    note = models.CharField(max_length=100, blank=True)

    # From here - Do not show to web page
    recoded_date = models.DateTimeField(auto_now=True)

    # Add author field later as ForeignKey
    # author = models.ForeignKey()

    def __str__(self):
        return self.name
