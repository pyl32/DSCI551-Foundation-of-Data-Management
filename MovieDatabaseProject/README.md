# MovieDB: Lightweight Database Engine (Relational + NoSQL) 🎬

A from-scratch database systems project built in Python that supports **SQL-like queries**, **file-based persistence**, and **chunked NoSQL storage** for scalable retrieval over a real dataset (~17K Netflix movie titles).

This project was developed as part of **DSCI551 Database Systems** and demonstrates core database concepts including **schema design, query parsing, joins, grouping/aggregation, indexing-style chunking, and CRUD operations**.

---

##  Summary

- Built a **custom Python database engine** supporting SQL-like operations:  
  `CREATE`, `INSERT`, `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, `UPDATE`, `DELETE`
- Designed a **file-backed NoSQL storage system** inspired by Firebase’s JSON tree model (schema-flexible, document-style data)
- Implemented **chunk-based storage (1000 records per chunk)** to enable scalable querying without loading the full dataset into memory
- Supported multiple join types: **inner / left / right / full joins**
- Added CLI interface for interactive querying and easy testing with scriptable commands

---

##  Motivation / Problem

Movie content datasets (like Netflix metadata) evolve frequently and contain semi-structured fields. Traditional relational design can become restrictive.

To address this, this project implements:
1) A relational-style query interface (SQL-like)  
2) A flexible NoSQL JSON-backed engine optimized for fast reads via chunked persistence  

The NoSQL dataset used includes **Netflix movie titles data (~17K movies)**.

---

## System Design

### NoSQL Engine (JSON Tree + Chunk Files)
- Each table stored as a directory under `nosql_data/`
- Each chunk stored as `chunk_0.json`, `chunk_1.json`, ...
- Designed to support:
  - schema inference / initialization
  - CRUD operations on disk
  - selection, filtering, projection, sorting, grouping

### Why Chunking?
Instead of storing 17K+ records in one massive JSON file, the dataset is split into **chunks of 1000 rows** to:
- avoid loading the entire dataset
- improve query performance by streaming chunk-by-chunk
- emulate how real databases scale storage

---

##  Tech Stack

- **Python** (core engine, CLI, storage layer)
- JSON + filesystem persistence
- CSV ingestion + chunk writer

---

##  Repository Structure

```
.
├── movie_titles.csv
├── create_tables_from_csv.py        # converts CSV to chunked JSON
├── nosql_data/                      # acts as file-based database
│   └── movie_titles/
│       ├── chunk_0.json
│       ├── chunk_1.json
│       └── ...
├── nosql_v4.py                      # main NoSQL DB engine + CLI
└── readMe.txt
```

---

## Getting Started

### 1) Build chunked tables from CSV
This converts the Netflix dataset into chunked JSON files:

```bash
python create_tables_from_csv.py
```

Chunks are written to:
```
./nosql_data/movie_titles/chunk_*.json
```

Chunk size defaults to **1000 records**.

---

### 2) Run the CLI database
```bash
python nosql_v4.py
```

Then you’ll see:

```
MyDB >
```

---

##  Supported Query Features (SQL-like)

### Create Table
```sql
create table movies (movie_id, title, year, director)
create table actors (actor_id, name, associated_movie_id, role)
```

### Insert
```sql
insert into movies movie_id=1; title='Inception'; year='2010'; director='Christopher Nolan'
insert into actors actor_id=1; name='Leonardo DiCaprio'; associated_movie_id=1; role='Cobb'
```

### Select + Filter
```sql
select from movies where year > '2000'
```

### Projection
```sql
select from movies project (title,director)
```

### Join (inner / left / right / full)
```sql
select from actors join movies on associated_movie_id=movie_id inner
select from movies join actors on movie_id=associated_movie_id left
select from actors join movies on associated_movie_id=movie_id right
select from movies join actors on movie_id=associated_movie_id full
```

### Group By + Aggregation
```sql
select from movies group by director aggregate count
```

### Ordering
```sql
select from movies order by year
```

### Update / Delete
```sql
update table movies set director='New Director' where title='Inception'
delete from movies where title='Unfilmed'
```

---

##  Testing

A test commands was applied.  
Example highlights:
- join + projection
- group/aggregation (`avg`, `count`)
- ordering
- update + delete

---

##  Future Improvements

- Add indexing (hash / B-tree) to accelerate `WHERE` queries
- Query optimization (predicate pushdown)
- Transaction layer for ACID properties (relational engine direction)
- Web demo UI (planned: Flask/React)

---

##  Team Members

- Yilin Pu – NoSQL database design
- Zhixin Zhao – Relational database design
- Xinyu Jiang – Web development implementation

---


## 📄 License
Academic project for DSCI551. Feel free to reference this repository for learning purposes(**but please do NOT copy/paste or submit this work as your own**).
