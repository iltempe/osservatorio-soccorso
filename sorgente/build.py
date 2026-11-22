import json, csv, io, os
base = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(base, "data.json"), encoding="utf-8"))
out = os.path.dirname(base); os.makedirs(os.path.join(out, "dati"), exist_ok=True)

# integrity checks
ids = {f["id"] for f in D["fonti"]}
for k in ["eventi","costi","quadro_economico","coperture","promesse","opere_collegate","cronoprogramma","fasi_cantiere","atti_finanziamento","documenti_progetto","gantt"]:
    for r in D[k]:
        for s in r["fonti"].split(","):
            assert s in ids, (k, s)
qe = sum(r["importo_eur"] for r in D["quadro_economico"])
cop = sum(r["importo_eur"] for r in D["coperture"])
print("QE somma", round(qe,2), "coperture", round(cop,2), "QE dichiarato", D["costi"][-1]["stima_eur"])
assert abs(qe-67310120.95)<0.01 and abs(cop-67310120.95)<0.01
used = set()
for k in ["eventi","costi","quadro_economico","coperture","promesse","opere_collegate","cronoprogramma","fasi_cantiere","atti_finanziamento","documenti_progetto","gantt"]:
    for r in D[k]: used |= set(r["fonti"].split(","))
print("fonti non usate:", sorted(ids-used))

def to_csv(rows, cols):
    b = io.StringIO(); w = csv.DictWriter(b, fieldnames=cols, lineterminator="\n"); w.writeheader()
    for r in rows: w.writerow({c: ("" if r.get(c) is None else r.get(c)) for c in cols})
    return b.getvalue()

src_url = {f["id"]: f["url"] for f in D["fonti"]}
def add_urls(rows):
    return [dict(r, fonti_url=" ".join(src_url[s] for s in r["fonti"].split(","))) for r in rows]

spec = {
 "eventi.csv": (add_urls(D["eventi"]), ["data","opera","fase","evento","importo_eur","fonti","fonti_url"]),
 "costi.csv": (add_urls(D["costi"]), ["data","stima_eur","cosa","fonti","fonti_url"]),
 "quadro_economico.csv": (add_urls(D["quadro_economico"]), ["voce","importo_eur","fonti","fonti_url"]),
 "coperture.csv": (add_urls(D["coperture"]), ["fonte_finanziaria","importo_eur","fonti","fonti_url"]),
 "promesse.csv": (add_urls(D["promesse"]), ["data_dichiarazione","chi","avvio_lavori_previsto","fonti","fonti_url"]),
 "opere_collegate.csv": (add_urls(D["opere_collegate"]), ["opera","ente","importo_eur","stato","nota","fonti","fonti_url"]),
 "cronoprogramma.csv": (add_urls(D["cronoprogramma"]), ["passo","stato","data_ufficiale","previsione_ufficiale","ritardo","fonti","fonti_url"]),
 "fasi_cantiere.csv": (add_urls(D["fasi_cantiere"]), ["fase","mesi","mesi_2018","cosa","fonti","fonti_url"]),
 "atti_finanziamento.csv": (add_urls(D["atti_finanziamento"]), ["atto","ente","data","importo_eur","fonti","fonti_url"]),
 "documenti_progetto.csv": (add_urls(D["documenti_progetto"]), ["documento","fase","fonti","fonti_url"]),
 "cronoprogramma_gantt.csv": (add_urls(D["gantt"]), ["gruppo","voce","tipo","inizio","fine","previsto","ritardo","nota","fonti","fonti_url"]),
 "fonti.csv": (D["fonti"], ["id","titolo","editore","tipo","url"]),
}
csvs = {}
for name,(rows,cols) in spec.items():
    s = to_csv(rows, cols); csvs[name] = s
    open(os.path.join(out,"dati",name),"w",encoding="utf-8").write(s)
json.dump(D, open(os.path.join(out,"dati","soccorso.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
html = open(os.path.join(base,"template.html"),encoding="utf-8").read()
html = html.replace("/*DATA*/", json.dumps(D, ensure_ascii=False)).replace("/*CSV*/", json.dumps(csvs, ensure_ascii=False))
open(os.path.join(out,"index.html"),"w",encoding="utf-8").write(html)
print("ok", len(D["eventi"]), "eventi,", len(D["fonti"]), "fonti")
