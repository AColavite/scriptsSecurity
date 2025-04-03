import shodan

API_KEY = "YOUR_SHODAN_API_KEY"  # Replace with your actual key
shodan_api = shodan.Shodan(API_KEY)

def search_shodan(query):
    try:
        results = shodan_api.search(query)
        print(f"Results found: {results['total']}\n")
        
        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Port: {result.get('port', 'N/A')}")
            print(f"Organization: {result.get('org', 'N/A')}")
            print(f"Operating System: {result.get('os', 'N/A')}")
            print(f"Data: {result['data']}\n")
            print("="*50)
    except shodan.APIError as e:
        print(f"Shodan API error: {e}")

query = input("Enter search query (e.g., 'apache'): ")
search_shodan(query)

