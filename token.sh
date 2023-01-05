echo "Get Auth Token : https://replicate.com/docs/reference/http#authentication "
read -p "Enter Token > " token
export REPLICATE_API_TOKEN="$token"
python run.py
