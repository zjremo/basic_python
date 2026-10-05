"""
Python 协程异步核心用法(asyncio)

同步：做一件事时线程被卡住，干不了别的(比如 time.sleep、普通 requests.get)。
异步：遇到 I/O 等待就让出控制权, 事件循环去跑别的协程, I/O 回来再继续。

三件套：
  1. async def  定义协程函数（调用它不会立刻执行，只得到 coroutine 对象）
  2. await      等待一个 awaitable(协程 / Task / Future)，并在等待时让出 CPU
  3. asyncio.run()  启动事件循环，跑入口协程（一般只在程序最外层调用一次）
"""

import asyncio
import time

async def fetch(name: str, delay: float) -> str:
    """模拟一次网络请求: sleep 期间不阻塞整个进程，只挂起当前协程。"""
    print(f"[{name}] start, will wait {delay}s")
    await asyncio.sleep(delay)  # 用 asyncio.sleep，不要用 time.sleep
    print(f"[{name}] done")
    return f"{name} result"


async def sequential() -> None:
    """顺序 await:总耗时 ≈ 各 delay 之和。"""
    t0 = time.perf_counter()
    a = await fetch("A", 1.0)
    b = await fetch("B", 1.0)
    print("sequential results:", a, b)
    print(f"sequential took {time.perf_counter() - t0:.2f}s\n")


async def concurrent_gather() -> None:
    """asyncio.gather: 几个协程并发跑，总耗时 ≈ 最慢的那个。"""
    t0 = time.perf_counter()
    a, b, c = await asyncio.gather(
        fetch("A", 1.0),
        fetch("B", 1.5),
        fetch("C", 0.5),
    )
    print("gather results:", a, b, c)
    print(f"gather took {time.perf_counter() - t0:.2f}s\n")


async def concurrent_tasks() -> None:
    """create_task: 把协程丢进事件循环立刻开始跑, 之后再 await 取结果。"""
    t0 = time.perf_counter()
    task_a = asyncio.create_task(fetch("task-A", 1.0))
    task_b = asyncio.create_task(fetch("task-B", 0.6))
    print("both tasks scheduled, doing other work...")
    await asyncio.sleep(0.2)
    results = await asyncio.gather(task_a, task_b)
    print("task results:", results)
    print(f"tasks took {time.perf_counter() - t0:.2f}s\n")


async def with_timeout() -> None:
    """wait_for: 给单次等待加超时。"""
    try:
        await asyncio.wait_for(fetch("slow", 2.0), timeout=0.5)
    except TimeoutError:
        print("with_timeout: too slow, cancelled\n")


async def main() -> None:
    print("=== sequential ===")
    await sequential()

    print("=== gather (concurrent) ===")
    await concurrent_gather()

    print("=== create_task ===")
    await concurrent_tasks()

    print("=== timeout ===")
    await with_timeout()


if __name__ == "__main__":
    asyncio.run(main())
