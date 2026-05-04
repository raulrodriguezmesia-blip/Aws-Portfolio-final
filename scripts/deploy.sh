# Deploy Script for AWS Portfolio
# This script copies the CV to the S3 bucket

BUCKET="cv-raul-rodriguez-mesa-2026"

echo "Deploying CV to AWS S3..."
aws s3 cp cv/index.html s3://$BUCKET/index.html --content-type "text/html"
echo "✅ Deployment complete!"
echo "URL: http://$BUCKET.s3-website-us-east-1.amazonaws.com"
