import grpc
import sys
from donica import text_sorter


# Getting mic stream audio into text
def get_text_to_speech_google(responses):
    try:
            print("talk")
            # text_rec
            num_chars_printed = 0
            for response in responses:
                if not response.results:
                    continue

                result = response.results[0]
                if not result.alternatives:
                    continue

                transcript = result.alternatives[0].transcript
                overwrite_chars = ' ' * (num_chars_printed - len(transcript))

                if not result.is_final:
                    sys.stdout.write(transcript + overwrite_chars + '\r')
                    sys.stdout.flush()
                    num_chars_printed = len(transcript)
                else:
                    get_mic = transcript+overwrite_chars
                    text_sorter.analyze_speech(get_mic)

                    num_chars_printed = 0
    except grpc.RpcError as e:
        if e.code() not in (grpc.StatusCode.INVALID_ARGUMENT,
                            grpc.StatusCode.OUT_OF_RANGE):
            raise e
        details = e.details()
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            if 'deadline too short' not in details:
                raise e
        else:
            if 'maximum allowed stream duration' not in details:
                raise e


def continuous_text_to_speech(responses, stream, resume):
    try:
        with_results = (r for r in responses if(
                r.results and r.results[0].alternatives))
        get_text_to_speech_google(
            _record_keeper(with_results, stream))
    except grpc.RpcError as e:
        if e.code() not in (grpc.StatusCode.INVALID_ARGUMENT,
                            grpc.StatusCode.OUT_OF_RANGE):
            raise
        details = e.details()
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            if 'deadline too short' not in details:
                raise
        else:
            if 'maximum allowed stream duration' not in details:
                raise

        print('Resuming..')
        resume = True


def _record_keeper(responses, stream):
        """Calls the stream's on_transcribe callback for each final response.
        Args:
            responses - a generator of responses. The responses must already be
                filtered for ones with results and alternatives.
            stream - a ResumableMicrophoneStream.
        """
        for r in responses:
            result = r.results[0]
            if result.is_final:
                top_alternative = result.alternatives[0]
                # Keep track of what transcripts we've received, so we can resume
                # intelligently when we hit the deadline
                stream.on_transcribe(duration_to_secs(
                    top_alternative.words[-1].end_time))
            yield r


def duration_to_secs(duration):
        return duration.seconds + (duration.nanos / float(1e9))

