# PRISMA 2020 Flow Diagram

## Textual Representation / Текстовое представление

```
┌─────────────────────────────────────────────────────────────┐
│  IDENTIFICATION                                             │
│  Идентификация                                              │
│                                                             │
│  Records identified from databases:                         │
│  • Google Scholar:                    342                   │
│  • eLibrary / РИНЦ:                   198                   │
│  • CNKI:                              264                   │
│                                                             │
│  TOTAL identified:                    804                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  SCREENING                                                  │
│  Скрининг                                                   │
│                                                             │
│  Records screened (title & abstract):     804               │
│                                                             │
│  Records excluded (title & abstract):   477               │
│  Reasons:                                                   │
│    • Non-relevant topic (not media analytics)               │
│    • No access to full text                                 │
│    • Non-academic publication type                          │
│    • Duplicate across databases                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  ELIGIBILITY                                                │
│  Доступность                                                │
│                                                             │
│  Full-text articles assessed:           327               │
│                                                             │
│  Full-text articles excluded:             0               │
│  (All assessed records met inclusion criteria)            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  INCLUDED — FINAL ANALYTICAL CORPUS                         │
│  Включено — итоговый аналитический корпус                   │
│                                                             │
│  Google Scholar:                        112                 │
│  eLibrary / РИНЦ:                        95                 │
│  CNKI:                                  120                 │
│                                                             │
│  TOTAL included:                        327                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  ADDITIONAL — EXTENDED RUSSIAN CORPUS                       │
│  Дополнительно — расширенный российский массив              │
│                                                             │
│  Extended RINC review:                  477                   │
│  (For deeper analysis of Russian contour)                   │
└─────────────────────────────────────────────────────────────┘
```

## Tabular Summary / Сводная таблица

| Stage | Google Scholar | РИНЦ | CNKI | Total | Notes |
|-------|---------------|------|------|-------|-------|
| **Identified** | 342 | 198 | 264 | **804** | Initial search across 3 databases |
| **Screened (title/abstract)** | 342 | 198 | 264 | **804** | Relevance screening |
| **Excluded (title/abstract)** | 230 | 103 | 144 | **477** | Non-relevant, no access, duplicates |
| **Full-text assessed** | 112 | 95 | 120 | **327** | Eligibility check |
| **Excluded (full-text)** | 0 | 0 | 0 | **0** | All met inclusion criteria |
| **Included (final corpus)** | 112 | 95 | 120 | **327** | Final analytical sample |
| **Additional corpus** | — | 477 | — | **477** | Extended RINC for depth |

## Inclusion Criteria / Критерии включения

1. Публикация посвящена системам медиааналитики, медиамониторинга или медиаметрии
2. Язык: русский, английский или китайский
3. Тип: научная статья, конференционный тезис, монография или аналитический отчёт
4. Период: 2019–2025 (для тематического анализа), 2019–2024 (для динамики DSS)
5. Доступ к полному тексту для кодирования

## Exclusion Criteria / Критерии исключения

1. Не связана с медиааналитикой (маркетинг без медиа, чистый IT)
2. Нет доступа к полному тексту
3. Неакадемический тип (новостная статья, блог)
4. Дублируется в другой базе данных
5. Не содержит анализируемого контента (только аннотация)

---

*PRISMA 2020 compliant / Соответствует PRISMA 2020*
*Diagram generated: 2026-05-14*
