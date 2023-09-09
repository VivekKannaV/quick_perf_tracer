from perfetto.trace_processor import TraceProcessor


def generate_report(trace_file, csv_dest_path):
    tp = TraceProcessor(trace_file)
    qr_it = tp.query('SELECT IMPORT("android.binder"); SELECT IMPORT("android.monitor_contention"); SELECT COALESCE(abt.client_process, amc.process_name) as process_name, amc.process_name AS contention_at, amc.is_blocking_thread_main, amc.is_blocked_thread_main, amc.short_blocking_method, amc.short_blocked_method, amc.blocking_thread_name, amc.blocked_thread_name, round(amc.dur/1000000.0, 2) AS durInMs, amc.blocking_thread_tid, amc.binder_reply_id FROM android_monitor_contention amc LEFT JOIN android_binder_txns abt ON amc.binder_Reply_id = abt.binder_reply_id WHERE (amc.process_name like \'com.trimble%\' OR abt.client_process like \'com.trimble%\') ORDER BY amc.process_name')
    qr_it.as_pandas_dataframe().to_csv(csv_dest_path + '/monitor_contention.csv')
    print("Successfully generated Contention report")

    qr_it = tp.query('SELECT aft.name as slice_id, apm.name as process_name, aft.layer_name, aft.dur  - 16666666 as delay , aft.jank_type, aft.display_frame_token as surface_flinger_slice_id, aft.ts FROM actual_frame_timeline_slice aft LEFT JOIN process apm ON aft.upid = apm.upid WHERE aft.dur > 16666666 AND aft.jank_type <> \'None\' AND aft.layer_name LIKE \'%com.trimble%\'')
    qr_it.as_pandas_dataframe().to_csv(csv_dest_path + '/jank.csv')
    print("Successfully generated Jank report")

    qr_it = tp.query('SELECT IMPORT("android.startup.startups"); SELECT package,  round(dur/1000000.0, 2) AS durInMs ,  ts, startup_type from android_startups')
    qr_it.as_pandas_dataframe().to_csv(csv_dest_path + '/starup.csv')
    print("Successfully generated Apps Startup report")
