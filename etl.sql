-- Allow etl_user to log in and set/reset password
ALTER ROLE etl_user WITH LOGIN;
ALTER USER etl_user WITH PASSWORD '12345';

-- Grant access to the database
GRANT ALL PRIVILEGES ON DATABASE etl_project TO etl_user;
GRANT USAGE ON SCHEMA public TO etl_user;
GRANT CREATE ON SCHEMA public TO etl_user;
GRANT ALL ON SCHEMA public TO etl_user;
