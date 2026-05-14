# Кодировочная книга исследования

## Назначение

Кодировочная книга описывает переменные, по которым размечались публикации в итоговой выборке. Она нужна для воспроизводимости исследования, проверки надежности кодирования и последующего расширения корпуса.

## Единица кодирования

Одна строка кодировочной матрицы = одна публикация или один источник.

## Основные переменные

| Переменная | Тип | Описание | Пример |
|---|---|---|---|
| id | string | Уникальный идентификатор записи | GS_001, RINC_001, CNKI_001 |
| database | categorical | База данных / источник | Google Scholar, РИНЦ, CNKI |
| contour | categorical | Аналитический контур | international, russian, chinese |
| year | integer | Год публикации | 2024 |
| language | categorical | Язык публикации | ru, en, zh |
| title | string | Название публикации | — |
| authors | string | Авторы | — |
| source_title | string | Журнал / конференция / сайт | — |
| doi | string | DOI при наличии | — |
| url | string | URL при наличии | — |
| system_mentioned | binary | Упоминается ли аналитическая система | 0/1 |
| system_name | string | Название системы | Brand Analytics, GDELT |
| dss_link | binary | Есть ли явная связь с DSS | 0/1 |
| dss_type | categorical | Тип DSS-связи | prediction, alerting, recommendation, management_cycle |
| analytical_mode | categorical | Режим работы с медиаданными | measurement, monitoring, osint_story, support_predictive, ai_native |
| analytical_product | categorical | Что производится аналитически | reach, narrative_map, event_reconstruction, forecast, recommendation |
| ai_component | categorical | Роль ИИ | none, auxiliary, core_layer |
| region_focus | categorical | Региональная привязка | Russia, China, global, mixed |
| inclusion_reason | string | Почему источник включен | — |
| exclusion_flag | binary | Исключен ли источник | 0/1 |
| exclusion_reason | string | Причина исключения | duplicate, irrelevant, no_media_data, no_metadata |
| coder_1 | string | Код первого кодировщика | — |
| coder_2 | string | Код второго кодировщика | — |
| agreement | binary | Совпадение кодировщиков | 0/1 |
| notes | string | Комментарии | — |

## Категории analytical_mode

### 1. measurement

**Описание:** измерение контакта аудитории с контентом: охват, доля, рейтинг, частота, внимание, контакт.

**Примеры систем:** Mediascope, Nielsen.

**Кодировать как measurement, если:** публикация фокусируется на аудитории, охватах, рейтингах, рекламной или медийной валюте.

### 2. monitoring

**Описание:** наблюдение за национальным или глобальным медиаполем, сбор упоминаний, выявление тем, тональности, нарративов.

**Примеры систем:** Brand Analytics, SCAN-Interfax, Factiva, LexisNexis, юйцин-платформы.

**Кодировать как monitoring, если:** основной результат — карта медиасистемы, мониторинг упоминаний, нарративов или репутационного поля.

### 3. osint_story

**Описание:** превращение медиаданных и открытых источников в реконструкцию событий, расследовательскую историю, цепочку влияния или объяснительный аналитический продукт.

**Примеры:** OSINT, data journalism, GDELT, расследовательские инструменты.

**Кодировать как osint_story, если:** публикация описывает реконструкцию событий, информационных кампаний, конфликтов фреймов или цепочек влияния.

### 4. support_predictive

**Описание:** использование медиаданных для предупреждения, прогнозирования, сценарного анализа, risk/reputation intelligence или рекомендации решения.

**Примеры систем:** Signal AI, Dataminr, Талисман, Wisers, Сина юйцин.

**Кодировать как support_predictive, если:** медиаданные прямо связываются с прогнозом, предупреждением, оценкой риска или решением.

### 5. ai_native

**Описание:** ИИ является основным intelligence layer, а не вспомогательным инструментом разметки.

**Примеры:** LLM reporting, Midu, AI-first risk intelligence platforms, исследовательские LLM pipelines.

**Кодировать как ai_native, если:** публикация/система строит аналитический продукт вокруг LLM/AI-слоя, автоматического извлечения сигнала или генерации отчетов.

## Правила кодирования DSS-связи

### dss_link = 1

Ставится, если есть хотя бы один признак:

- decision support / поддержка принятия решений;
- prediction / прогнозирование;
- early warning / предупреждение;
- risk scoring / оценка риска;
- recommendation / рекомендация действия;
- integration into management cycle / интеграция в управленческий цикл;
- scenario planning / сценарное проектирование.

### dss_link = 0

Ставится, если публикация ограничивается:

- мониторингом;
- подсчетом упоминаний;
- визуализацией данных;
- описанием инструментов;
- анализом тональности без перехода к действию;
- общим обсуждением ИИ без decision-making компонента.

## Надежность кодирования

В статье указаны значения:

- Cohen’s Kappa = 0.84 для тематической классификации;
- Cohen’s Kappa = 0.91 для определения DSS-связи.

Для репозитория рекомендуется добавить файл `data/derived/intercoder_reliability.csv` с агрегированными результатами кодирования.
