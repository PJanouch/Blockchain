# Můj blockchain

Tohle je takovej můj pokus o vlastní blockchain s REST API přes Flask. Je to úplný základ – třída na chain a pár API, aby se s tím dalo pracovat.

## Obsah
- [Co tu najdete](#co-tu-najdete)
- [Spuštění](#spuštění)
- [Endpointy](#endpointy)
- [Závěr](#závěr)

## Co tu najdete
Prostě jsem si chtěl zkusit napsat vlastní blockchain v Pythonu a pochopit, jak to pod kapotou funguje. 

## Spuštění
1. Musíš mít nainstalovaný Python
2. Stáhni si Flask: `pip install flask`
3. Spusť to: `python blockchain.py`

## Endpointy
Můžete si zkusit tyto cesty:
* `/mine` (GET) - vytěží to nový blok
* `/transactions/new` (POST) - přidá to novou transakci
* `/chain` (GET) - vypíše to celý aktuální chain

## Závěr
Tento kód je sestrojen vlastnoruční prací a pokud najdete nějaké chyby, budu rád za feedback!
