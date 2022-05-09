from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

from joblib import Parallel, delayed
from tqdm import tqdm


def thread_executor(method, data):
    """
    Разделяет задачу на множество подзадач в многопотоке
    :param method: метод, в котором будет выполняться 1 поток
    :param data: данные, которые будут доступны в методе
    """
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        return list(tqdm(executor.map(method, data), total=len(data), smoothing=0.05))
        # tqdm(executor.map(method, data), total=len(data))


def parallel(method, data):
    return Parallel(n_jobs=cpu_count())(delayed(method)(i) for i in data)


def flat_list(t):
    return [item for sublist in t for item in sublist]
