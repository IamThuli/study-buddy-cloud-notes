Study Buddy Cloud Notes
A serverless note-sharing app built on AWS Cloud to help South African students collaborate and access study notes easily.

🌍 Problem Statement
Many South African students struggle with:

Losing notes across devices.

Limited access to structured study platforms.

Expensive learning tools.

Study Buddy Cloud Notes solves this by offering a free, cloud-hosted platform for uploading and retrieving study notes.

🚀 Features
✅ Upload text notes and get a unique Note ID.
✅ Retrieve notes anytime using the Note ID.
✅ Hosted entirely on AWS Free Tier using serverless services.
✅ Lightweight frontend for easy access via browser.

🏗️ Architecture
graph TD
  A[Student Browser] -->|Upload/Fetch| B(API Gateway)
  B --> C[Lambda: Upload Note]
  B --> D[Lambda: Fetch Note]
  C --> E[S3 Bucket: Store Notes]
  D --> E
  E --> B
  B --> A
⚙️ Tech Stack
AWS S3 → Static website + note storage

AWS Lambda → Business logic (upload/fetch)

AWS API Gateway → API endpoints

Python (Boto3) → Lambda functions

HTML + JavaScript → Frontend

📂 Project Structure
study-buddy-cloud-notes/
│── frontend/
│   └── index.html       # Simple upload & fetch UI
│── backend/
│   ├── lambda_upload.py # Lambda for uploading notes
│   ├── lambda_fetch.py  # Lambda for fetching notes
│   └── template.yaml    # Infra-as-code (optional SAM template)
│── README.md            # Documentation
⚡ Deployment Guide
1️⃣ Clone Repo
git clone https://github.com/<your-username>/study-buddy-cloud-notes.git
cd study-buddy-cloud-notes
2️⃣ Setup S3 Bucket
aws s3 mb s3://study-buddy-notes-<yourname>
aws s3 website s3://study-buddy-notes-<yourname>/ --index-document index.html
3️⃣ Deploy Lambdas
Upload lambda_upload.py and lambda_fetch.py to AWS Lambda.
Make sure to set an S3 Bucket name inside each Lambda file.

4️⃣ Setup API Gateway
/upload → POST → Lambda (Upload)

/fetch → GET → Lambda (Fetch)

Enable CORS

5️⃣ Update Frontend
In frontend/index.html, replace:

const API_BASE = "YOUR_API_GATEWAY_URL";
6️⃣ Upload Frontend to S3
aws s3 cp frontend/index.html s3://study-buddy-notes-<yourname>/
7️⃣ Test
Open your S3 static site URL in browser.

Upload a note → Copy Note ID → Fetch → 🎉

🎯 Future Enhancements
🔐 Add authentication with AWS Cognito (only students can upload).

📊 Use DynamoDB to store metadata (author, subject, date).

📱 Build a mobile-friendly UI (React/Flutter).

🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.

🌟 Acknowledgments
Inspired by the need to bridge digital gaps for South African students.

Built in under 2 hours using AWS Free Tier.

⚡ Tip: Once deployed, update your README with:

✅ Live Demo URL (S3 website link).

✅ API Gateway URL (for devs).

✅ Screenshots/GIF of your app in action.
