--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: table_test; Type: TABLE; Schema: public; Owner: db_project
--

CREATE TABLE public.table_test (
    id integer NOT NULL,
    type character varying(50) NOT NULL
);


ALTER TABLE public.table_test OWNER TO db_project;

--
-- Data for Name: table_test; Type: TABLE DATA; Schema: public; Owner: db_project
--

COPY public.table_test (id, type) FROM stdin;
\.


--
-- Name: table_test_pkey; Type: CONSTRAINT; Schema: public; Owner: db_project
--

ALTER TABLE ONLY public.table_test
    ADD CONSTRAINT table_test_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

