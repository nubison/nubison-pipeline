class NubisonPipeline:
    def __init__(self, name: str, version: str = "0.1.0"):
        self.name = name
        self.version = version

    def run(self, data_path: str, **kwargs):
        return {
            "pipeline_name": self.name,
            "pipeline_version": self.version,
            "status": "success",
        }
