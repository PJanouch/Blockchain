# Můj první Blockchain

Vítejte v mém repozitáři! Zde najdete ukázku jednoduchého blockchainu s REST API, který využívá framework Flask.

## Obsah
- [O projektu](#o-projektu)
- [Jak to spustit](#jak-to-spustit)
- [Struktura API](#struktura-api)
- [Závěr](#závěr)

## O projektu
Tento projekt je ukázkou toho, jak funguje distribuovaná účetní kniha. Obsahuje třídu pro samotný blockchain a několik endpointů pro komunikaci se sítí.

## Jak to spustit
1. Ujistěte se, že máte nainstalovaný Python.
2. Nainstalujte potřebnou knihovnu pomocí příkazu: `pip install flask`
3. Spusťte hlavní soubor: `python blockchain.py`

## Struktura API
Aplikace má připravené tyto základní cesty k vyzkoušení:
* `/mine` (GET) - Slouží k vytěžení nového bloku.
* `/transactions/new` (POST) - Slouží k přidání nové transakce.
* `/chain` (GET) - Vrátí celý aktuální řetězec bloků.

## Závěr
Tento kód je sestrojen vlastnoruční prací a pokud najdete nějaké chyby, budu rád za feedback!
