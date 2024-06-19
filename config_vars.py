import spb.sdk

DATA_PATH = "./data"
DATA_DIRS = [
    "./data/images",
    "./data/yolo_labels",
]
IMAGES_PATH = DATA_DIRS[0]
YOLO_LABELS_PATH = DATA_DIRS[1]
METADATA_PATH = DATA_PATH + "/meta/default_dataset"

LABELS_LINKS = {
    "corona.zip" : "https://suite-civet-export-us-east-1-prod-s3.s3-accelerate.amazonaws.com/intuitivo-dev/a7849f85-3126-46c1-97ce-97aaeb99f978/fd6f6678-d828-4032-b2c2-a4a6aeba39d1/6_showroom_in2_data_collection_annotations_2022-12-12.zip?response-content-disposition=attachment%3B%20filename%3Dapproved%20-%20corona.zip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQEBLWAF4MHNVWFQ2%2F20230714%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230714T183030Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDiDMwL6bCudvrWCHTP3iITrcTJ7vfVNzEBwtPYWKafUgIhAM6ENp36hgmz7oIzlHlVY1EI1WHSvDItnDTwb4n31bBzKoMECBoQAhoMMDA4NjgxNTU0Mjk2IgzSs5kSBHAk%2FimSaywq4AORMyt3xx%2Foiw%2BS22TgAFmn7PyJwDAwK%2BZTJe2cX2YNPNt8w7RNhS%2FiMtcrIlB%2BtSUcPLF75VxNVMcVj4BTFgPrE%2BmrPjt5kQn7hslhqCmnZk92SyB0mpL3iagnjhdx8BfYdqHgSJBdsXiOyMgimmqUCFvJkxwCdu8jM8IQ%2B7TRNlSIphISKG6YM91jw8fZAsIS84jpnF%2Fq97an1f6CXdTNxjyIhdA4wfJ%2Bd8TEnps3yGFcNEoVoLo7FZoj0KEjh2gam53KHEF317d2qKgbLtbbXHT7WkIcgv7yCK5jOr4fGCegUcLBeA3REPrI6VY0KLsL89qF5v%2FtmIxBJ3RAEjobldsVHB5FlZlAfztYg4l4EPLZZpXYV1c5epuS5tOi%2Fba240wnt2u3b95AvBe%2Bf4IlgPE1DRqHA7AslmrpqMg9gFbE6ioJ8%2F8PlWSfdx77LFbvQPhXfrckAbrU9HM6QCczF2w70ChF3IzxAmyrJiHQryKTRXifhkSUZI44VKuarT0k6lxZTWO2NSuycyCXXQdHDIjesfLTeaEDqhj0GTcjsuHsr3z3tOAVlzP0BaOL29VBUKeyugDEELhoY%2BGMODEC0uKJQU%2BAC9q1acejVkSjI4UsOn5BToCMWn7dA6slLd4w2fzFpQY6pAGpuz3E%2FNdKClFJ7Skj5Puce1Mu7acNAuzbTouujR6nskoYZYMfe2MeLj8vWnK0lEG3wnm2bI%2BnSZCJGjPTTpmy%2FyOPgGmKXp2SJl2%2ByxJTfAxcxXfvp29E5y18Gdhn3%2BO0RiyEljaE5xJFhwmWRY1RfmpPIZE62W4wASNY9XlpngCheIq9Z97dMZ1S1%2FU3VorVWQFpnegQLuqRHEMnR4aWjxJV6Q%3D%3D&X-Amz-Signature=cd69e6e104f35c56fd9da654a6f51f7ba5acde013ce89c2e74611db6d7636cd0",
    "budweiser.zip" : "https://suite-civet-export-us-east-1-prod-s3.s3-accelerate.amazonaws.com/intuitivo-dev/a7849f85-3126-46c1-97ce-97aaeb99f978/2063177f-1cf2-4981-b13e-02cc7a8a1ef2/7_showroom_in2_data_collection_annotations_2022-12-12.zip?response-content-disposition=attachment%3B%20filename%3Dapproved%20-%20budweiser.zip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQEBLWAF4EHSZ7O5U%2F20230714%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230714T183016Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIAS0XNzSuv3YYXeOphcKk6FXL5HAguuX1FUwtzQDxrUyAiAfJR2pHPYFRsL42oyLcb1s%2FM9fSy2T7wgR5g1GISxwZiqDBAgaEAIaDDAwODY4MTU1NDI5NiIMmdH08Cbb%2BFs26SCxKuADzjRf%2FARMnX1mUz6VNVDYaonytIc5CYWRdPQnq0Yo5AaXuMf0tQbSOiaw82IWVFFE6O%2Bxrl5wkMFQHIO2ZtyFOlcz0qUlyX%2BcOBSbmKYJJ5nErnJjwqsCexwtI8gaWfXGz8Qlg0VvdoB7%2Bc411L%2BU5YhDMD%2FwlY8V1IQk8fHBJgtBRik1NU3fiehiCddPz9%2F48%2FQotkonKUnOMGhkCbcFyW%2FbfYBTfp01X4NoGPBLf6xb2toZkouplGLJ4pCFJwtfDshS9RJ4K0ts4f8VPt%2Bh7Suf2ZHp3vV%2BGMPOeBc6I3PNydpUOudkaK5IA9xEsqJSM4HsuB25wEiYQ4mSD2EKt2ryMgB5DWKsRcWjKhOYIgS%2F9SIQtsHmLoLKfvq9Yrp09lqUUnZGJETur402WJRrHVIbVrXQzaDtBnEnMRdore3EkgWeut0mNMwOn5oNV%2BSsaq3maKMfrcohpSpCzUfuYSCXIeDnSKg%2BqCbvpgaRX30vhG8SK5OPgzU8GiVYatmCrYxOn%2FvpTB8APsEV%2FySaY2GJow8Z6YqphX9F%2BDe1eXAjiJQ58SkWfEsDtzpWg3eA6Q5F9gc940glTZAnBgFC1yUAMrIHL2chjaSYpYkuJE91ahKakiioIU4JHQr3fBidMO%2F5xaUGOqYBMhlCdY%2F%2F5IYM3qMImka5nwqUDN82vt8qEQ1JkHbokM936Sc8CaOAn73lQ0GvjrzIYUavctEEkCEwj5hHNvuEso%2B7gpx6uOXywyIWhjM41eKiOR2K0HtxPzP1EM%2BORR7e63sZMDucTLVJx%2F2e%2FssCpsyrQZZ5dG7eT3rJez2heKbC1Mqr3HliqmiFCionC7GBILAfdP5YeFCbtzsElxhejnujJwryOA%3D%3D&X-Amz-Signature=3c44d36b151d73407db823efeaf5129d9206027091d84e4fff7bfa9b7b169524",
    "heineken.zip" : "https://suite-civet-export-us-east-1-prod-s3.s3-accelerate.amazonaws.com/intuitivo-dev/a7849f85-3126-46c1-97ce-97aaeb99f978/f2aaba16-e40f-4bf4-9c9c-fd24856a1d56/8_showroom_in2_data_collection_annotations_2022-12-12.zip?response-content-disposition=attachment%3B%20filename%3Dapproved%20-%20heineken.zip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQEBLWAF4EHSZ7O5U%2F20230714%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230714T183002Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIAS0XNzSuv3YYXeOphcKk6FXL5HAguuX1FUwtzQDxrUyAiAfJR2pHPYFRsL42oyLcb1s%2FM9fSy2T7wgR5g1GISxwZiqDBAgaEAIaDDAwODY4MTU1NDI5NiIMmdH08Cbb%2BFs26SCxKuADzjRf%2FARMnX1mUz6VNVDYaonytIc5CYWRdPQnq0Yo5AaXuMf0tQbSOiaw82IWVFFE6O%2Bxrl5wkMFQHIO2ZtyFOlcz0qUlyX%2BcOBSbmKYJJ5nErnJjwqsCexwtI8gaWfXGz8Qlg0VvdoB7%2Bc411L%2BU5YhDMD%2FwlY8V1IQk8fHBJgtBRik1NU3fiehiCddPz9%2F48%2FQotkonKUnOMGhkCbcFyW%2FbfYBTfp01X4NoGPBLf6xb2toZkouplGLJ4pCFJwtfDshS9RJ4K0ts4f8VPt%2Bh7Suf2ZHp3vV%2BGMPOeBc6I3PNydpUOudkaK5IA9xEsqJSM4HsuB25wEiYQ4mSD2EKt2ryMgB5DWKsRcWjKhOYIgS%2F9SIQtsHmLoLKfvq9Yrp09lqUUnZGJETur402WJRrHVIbVrXQzaDtBnEnMRdore3EkgWeut0mNMwOn5oNV%2BSsaq3maKMfrcohpSpCzUfuYSCXIeDnSKg%2BqCbvpgaRX30vhG8SK5OPgzU8GiVYatmCrYxOn%2FvpTB8APsEV%2FySaY2GJow8Z6YqphX9F%2BDe1eXAjiJQ58SkWfEsDtzpWg3eA6Q5F9gc940glTZAnBgFC1yUAMrIHL2chjaSYpYkuJE91ahKakiioIU4JHQr3fBidMO%2F5xaUGOqYBMhlCdY%2F%2F5IYM3qMImka5nwqUDN82vt8qEQ1JkHbokM936Sc8CaOAn73lQ0GvjrzIYUavctEEkCEwj5hHNvuEso%2B7gpx6uOXywyIWhjM41eKiOR2K0HtxPzP1EM%2BORR7e63sZMDucTLVJx%2F2e%2FssCpsyrQZZ5dG7eT3rJez2heKbC1Mqr3HliqmiFCionC7GBILAfdP5YeFCbtzsElxhejnujJwryOA%3D%3D&X-Amz-Signature=b8a8bfb0a19f9692f0694a06de36c3472a8064eaf0a3aed40b1e284092eb6d72",
    "stella.zip" : "https://suite-civet-export-us-east-1-prod-s3.s3-accelerate.amazonaws.com/intuitivo-dev/a7849f85-3126-46c1-97ce-97aaeb99f978/7c4cbf17-c7d6-4a6d-a1c9-81fe3fca9760/9_showroom_in2_data_collection_annotations_2022-12-12.zip?response-content-disposition=attachment%3B%20filename%3Dapproved%20-%20stella.zip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQEBLWAF4MHNVWFQ2%2F20230714%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230714T182945Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDiDMwL6bCudvrWCHTP3iITrcTJ7vfVNzEBwtPYWKafUgIhAM6ENp36hgmz7oIzlHlVY1EI1WHSvDItnDTwb4n31bBzKoMECBoQAhoMMDA4NjgxNTU0Mjk2IgzSs5kSBHAk%2FimSaywq4AORMyt3xx%2Foiw%2BS22TgAFmn7PyJwDAwK%2BZTJe2cX2YNPNt8w7RNhS%2FiMtcrIlB%2BtSUcPLF75VxNVMcVj4BTFgPrE%2BmrPjt5kQn7hslhqCmnZk92SyB0mpL3iagnjhdx8BfYdqHgSJBdsXiOyMgimmqUCFvJkxwCdu8jM8IQ%2B7TRNlSIphISKG6YM91jw8fZAsIS84jpnF%2Fq97an1f6CXdTNxjyIhdA4wfJ%2Bd8TEnps3yGFcNEoVoLo7FZoj0KEjh2gam53KHEF317d2qKgbLtbbXHT7WkIcgv7yCK5jOr4fGCegUcLBeA3REPrI6VY0KLsL89qF5v%2FtmIxBJ3RAEjobldsVHB5FlZlAfztYg4l4EPLZZpXYV1c5epuS5tOi%2Fba240wnt2u3b95AvBe%2Bf4IlgPE1DRqHA7AslmrpqMg9gFbE6ioJ8%2F8PlWSfdx77LFbvQPhXfrckAbrU9HM6QCczF2w70ChF3IzxAmyrJiHQryKTRXifhkSUZI44VKuarT0k6lxZTWO2NSuycyCXXQdHDIjesfLTeaEDqhj0GTcjsuHsr3z3tOAVlzP0BaOL29VBUKeyugDEELhoY%2BGMODEC0uKJQU%2BAC9q1acejVkSjI4UsOn5BToCMWn7dA6slLd4w2fzFpQY6pAGpuz3E%2FNdKClFJ7Skj5Puce1Mu7acNAuzbTouujR6nskoYZYMfe2MeLj8vWnK0lEG3wnm2bI%2BnSZCJGjPTTpmy%2FyOPgGmKXp2SJl2%2ByxJTfAxcxXfvp29E5y18Gdhn3%2BO0RiyEljaE5xJFhwmWRY1RfmpPIZE62W4wASNY9XlpngCheIq9Z97dMZ1S1%2FU3VorVWQFpnegQLuqRHEMnR4aWjxJV6Q%3D%3D&X-Amz-Signature=0d3699ba46ac02863c21195707a1b551883daa6d8d46f54e2bc6fc9f2fd99dc1"
}
CLASSES = {
    "corona_355_ml_1234": 0,
    "budweiser_long_neck_1236": 1,
    "heineken_long_neck_1238": 2,
    "stella_artois_1235": 3,
    "pepsi_2l_1230": 4,
    "coca_cola_1,5l_1239": 5 
}

SPB_DATASET = "showroom_in2_data_collection_annotations"
SPB_CLIENT = spb.sdk.Client(project_name=SPB_DATASET)