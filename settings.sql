CREATE DATABASE child_care;
CREATE USER child_careuser
WITH PASSWORD 'password';
ALTER ROLE child_careuser
SET client_encoding TO 'utf8';
ALTER ROLE child_careuser
SET default_transaction_isolation TO 'read committed';
ALTER ROLE child_careuser
SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE child_care TO child_careuser;