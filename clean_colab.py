import nbformat as nbf

in_path = "BestVerie_RetailBanking_Assistant.ipynb"   # change to your file name
out_path = "BestVerie_RetailBanking_Assistant_clean.ipynb"

nb = nbf.read(in_path, as_version=4)

# Remove problematic widget metadata
if "widgets" in nb.metadata:
    nb.metadata.pop("widgets", None)
# Some notebooks store widget state here too:
nb.metadata.pop("widget_state", None)
nb.metadata.pop("widget_manager_state", None)

# Also remove per-cell widget metadata if present
for cell in nb.cells:
    if "metadata" in cell and isinstance(cell["metadata"], dict):
        cell["metadata"].pop("widgets", None)

nbf.write(nb, out_path)
print("Wrote:", out_path)