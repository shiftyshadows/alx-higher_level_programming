import importlib.util

if __name__ == "__main__":
    module_name = "variable_load_5"
    module_path = "./variable_load_5.py"

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    a = getattr(module, "a")
    print(a)
