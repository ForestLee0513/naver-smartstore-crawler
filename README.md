# NAVER Smartstore(brand) product info crawler

네이버 스마트스토어(브랜드스토어)의 상품 정보를 가져오는 크롤러입니다.
해당 크롤러는 상품의 상품의 품절 여부 확인에 최적화 되어있습니다.

## 사용법

### GET /get-products

여러 상품의 정보를 요청합니다.

- body

```json
{
    "url": ["string", "string", ...]
}
```
