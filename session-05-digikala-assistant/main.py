from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/digikal/search", status_code=200)
async def digikalaSearch(
   input: Request
):
    url = f"https://api.digikala.com/v1/search/?{input.query_params}"
    response = requests.get(url, allow_redirects=False)
    products = response.json().get("data", {}).get("products",[])
    # Extracting specific properties from each product
    filtered_products = []
    for product in products:
        filtered_products.append({
            "id": product.get("id"),
            "title_fa": product.get("title_fa"),
            "url": product.get("url", {}).get("uri"),
            "images": {
                "main": {
                    "url": product.get("images", {}).get("main", {}).get("url", []),
                    "webp_url": product.get("images", {}).get("main", {}).get("webp_url", [])
                }
            },
            "rating": product.get("rating", {})
        })

    # Now `filtered_products` contains only the required properties
    return filtered_products
    