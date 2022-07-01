class Merge_Dataset(Dataset):
    def __init__(self, adata_raw, adata_filtered):
        self.rna_data_filtered, self.atac_data_filtered = self._load_merge_data(adata_filtered)
        self.rna_data_raw = self._load_raw_ref_data(adata_raw)

    def __len__(self):
        # here, i have to normalise PPG & matrices of phonems
        # assert(len(self.rna_data) == len(self.atac_data))
        return len(self.atac_data_filtered)

    def __getitem__(self, idx):
        rna_filtered = self.rna_data_filtered.values[idx]
        atac_filtered = self.atac_data_filtered.values[idx]
        rna_raw = self.rna_data_raw.values[idx]
        # return a tensor that for a single observation
        return [
            torch.from_numpy(rna_filtered).float(),
            torch.from_numpy(atac_filtered).float(),
            torch.from_numpy(rna_raw).float(),
        ]

    def _load_merge_data(self, adata):
        rna_df = pd.DataFrame(
            data=adata.X.toarray(),
            index=np.array(adata.obs.index),
            columns=np.array(adata.var.index),
        )
        atac_df = pd.DataFrame(
            data=adata.obsm["mode2"].toarray(),
            index=np.array(adata.uns["mode2_obs"]),
            columns=np.array(adata.uns["mode2_var"]),
        )
        return rna_df, atac_df

    def _load_raw_ref_data(self, adata_raw):
        rna_df = pd.DataFrame(
            data=adata_raw.X.toarray(),
            index=np.array(adata_raw.obs.index),
            columns=np.array(adata_raw.var.index),
        )
        return rna_df