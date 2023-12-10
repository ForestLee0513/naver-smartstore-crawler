# NAVER Smartstore(brand) product info crawler

네이버 스마트스토어(브랜드스토어)의 상품 정보를 가져오는 크롤러입니다.
해당 크롤러는 상품의 상품의 재입고 여부 확인에 최적화 되어있습니다.

## 사용법

### GET /get-products

여러 상품의 정보를 요청합니다.

- body

```json
{
    "url": ["string", "string", ...]
}
```

## TODO

- [ ] 멀티스레딩 적용하여 크롤링 속도 개선
- [ ] 재입고 알림기능이 없는 다른 쇼핑몰도 추가할 수 있도록 프로젝트 폴더구조 개선
