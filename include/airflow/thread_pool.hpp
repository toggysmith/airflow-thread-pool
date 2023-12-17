#ifndef AIRFLOW_THREAD_POOL_HPP
#define AIRFLOW_THREAD_POOL_HPP

namespace airflow {
	/**
	 * @brief Facilitates the creation and management of a thread pool.
	 *
	 * This class provides facilities for the creation of a
	 * thread pool and submitting workloads onto that thread
	 * pool. A thread pool is a group of pre-instantiated,
	 * idle threads which stand ready to be given work.
	 *
	 * Thread objects require a large amount of memory and
	 * continually allocating/deallocating them incurs a
	 * significant memory management overhead which can be
	 * avoided with thread pools.
	 *
	 * For example, say you had a game with enemies
	 * constantly attacking a player, the enemies respawn
	 * after dying, there's never more than 50 enemies, and
	 * each enemy AI is running on its own thread. This
	 * would be an excellent use case for a thread pool
	 * because rather than deallocating a dead enemy's
	 * thread, we can reuse it for the enemy that respawns
	 * to replace it. This avoids the costly
	 * deallocation/allocation process.
	 */
	class ThreadPool {};
}

#endif
