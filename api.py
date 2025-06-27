import requests

get_url= "https://jsonplaceholder.typicode.com/posts/1"
response_get = requests.get(get_url)
print("GET Request Response:")
print("Status Code:",response_get.status_code)

#POST Request
post_url = "https://jsonplaceholder.typicode.com/posts"

#Data to  be sent in the POST Request
post_data ={
    "title":"My New Post",
    "body":"This is the content of the post.",
    "userId":1
 }

response_post = requests.post(post_url,json=post_data)
print("Post Request Response.")
print("status code:",response_post.status_code)
print("Data:",response_post.json())