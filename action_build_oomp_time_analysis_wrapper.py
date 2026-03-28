import action_build_oomp



import cProfile
import pstats
import action_build_oomp
import os

def main(**kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Your main function code here
    action_build_oomp.main(**kwargs)  # Replace with the actual function call
    
    profiler.disable()
    stat_file = 'temporary/profile_output.prof'
    profiler.dump_stats(f'{stat_file}')
    print(f"Profiling data saved to {stat_file}")

    #launch visualizer
    os.system(f'snakeviz {stat_file}')
 


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)