CREATE DATABASE child_care;
CREATE USER child_careuser
WITH PASSWORD 'child_care';
GRANT ALL PRIVILEGES ON DATABASE child_care TO child_careuser;