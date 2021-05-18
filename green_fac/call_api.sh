 curl -X POST "http://127.0.0.1:8000/nlp/v1/coreference" \
 -H "Content-Type: application/json" \
 -d '{
       "context": ["今天晚上有马刺队的比赛，他们的对手是湖人队",
                   "没想到你也看篮球"
       ],
       "text": "我还是他们的粉丝呢"}'


curl -X POST "http://10.177.34.157:8000/nlp/v1/chat" \
-H "Content-Type: application/json" \
-d '{"text": "想你了"}'
