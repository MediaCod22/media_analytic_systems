# Raw data placeholder

Эта папка предназначена для исходных выгрузок из Google Scholar, eLibrary/РИНЦ и CNKI.

## Рекомендуемая структура

```text
data/raw/
├── google_scholar/
│   ├── search_results_YYYY-MM-DD.csv
│   └── notes.md
├── rinc/
│   ├── search_results_YYYY-MM-DD.csv
│   └── notes.md
└── cnki/
    ├── search_results_YYYY-MM-DD.csv
    └── notes.md
```

## Важно

Если условия использования базы данных не позволяют публиковать полные выгрузки, можно оставить только:

- библиографические метаданные включенных публикаций;
- агрегированные таблицы;
- кодировочную матрицу без защищенного контента;
- описание поисковых запросов и дат поиска.
