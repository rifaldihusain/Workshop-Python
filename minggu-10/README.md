# minggu-10

# Build a Python App  database with [CockroachDB](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb.html)

1. Download and extract the [CockroachDB v2.1.1 archive for Windows](https://binaries.cockroachdb.com/cockroach-v2.1.1.windows-6.2-amd64.zip)

2. - cockroach.exe version -> melihat versi dari CockroachDB
   - start cockroach.exe   -> menjalankan CockroachDB
   
   ![Gambar 1](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/1.PNG)

# masuk ke Start a Local Cluster [Insecure](https://www.cockroachlabs.com/docs/stable/start-a-local-cluster.html)

1. $cockroach start --insecure --listen-addr=localhost
	
   ![Gambar 2](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/2.PNG)
	
2. - In a new terminal, add the second node:
   ```$cockroach start \
      --insecure \
	  --store=node2 \
	  --listen-addr=localhost:26258 \
	  --http-addr=localhost:8081 \
	  --join=localhost:26257
	```
	
	- In a new terminal, add the third node:
	```$cockroach start \
	   --insecure \
	   --store=node3 \
	   --listen-addr=localhost:26259 \
	   --http-addr=localhost:8082 \
	   --join=localhost:26257
	```

3. Test the cluster -> membuat database

   ![Gambar 3](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/3.PNG)
	
# [Build a Python App with CockroachDB](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb.html#insecure)

1. Install the psycopg2 driver

   ![Gambar 4](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/4.PNG)
   
2. Create the ```maxroach``` user and ```bank``` database

   ![Gambar 5](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/5.PNG)
   
3. Run the Python code

   - buat configurasi dengan nama ```basic-sample.py```
   - jalankan ```basic-sample.py```

   ![Gambar 6](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/6.PNG)
   
   - buat configurasi dengan nama ```txn-sample.py```
   - jalankan ```txn-sample.py```
   - To verify that funds were transferred from one account to another, start the built-in SQL client
   - To check the account balances, issue the following statement:
   
   ![Gambar 7](https://github.com/rifaldihusain/workshop-python/blob/master/minggu-10/src/7.PNG)