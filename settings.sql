CREATE DATABASE child_care;
CREATE USER child_careuser
WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE child_care TO child_careuser;