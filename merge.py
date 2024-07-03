from binidx import MMapIndexedDatasetBuilder, index_file_path, MMapIndexedDataset
import numpy as np

out_file = f"/bigtemp/bfr4xr/uncopyright_pile/pile"
db = MMapIndexedDatasetBuilder(out_file=out_file + ".bin", dtype=np.uint16)

start_index = 0
end_index = 30

for num in range(start_index, end_index):
    data = f"/bigtemp/bfr4xr/json2binidx_tool/data/{num}_text_document"
    index = MMapIndexedDataset.Index(index_file_path(data))
    db.merge_file_(data)

db.finalize(out_file + ".idx")



# merge pile-0,1,2 to a big single file
#out_file = f"/bigtemp/bfr4xr/pile/pile"
#db = MMapIndexedDatasetBuilder(out_file=out_file + ".bin", dtype=np.uint16)
#for num in range(0, 3):
#    data = f"/bigtemp/bfr4xr/pile/pile-{num}"
#    index = MMapIndexedDataset.Index(index_file_path(data))
#    db.merge_file_(data)
#
#db.finalize(out_file + ".idx")
