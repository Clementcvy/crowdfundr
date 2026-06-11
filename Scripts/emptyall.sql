DO $$ DECLARE
    table_name text;
BEGIN
    FOR table_name IN (SELECT tablename FROM pg_tables WHERE schemaname='sql') LOOP
        EXECUTE 'TRUNCATE TABLE ' || 'sql.'||table_name || ' CASCADE;';
    END LOOP;
END $$;