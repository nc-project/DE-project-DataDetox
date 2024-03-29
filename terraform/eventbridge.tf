resource "aws_cloudwatch_event_rule" "lambda_trigger_rule" {
  name                = "lambda-every-5-minute"
  description         = "retry scheduled every 5 min"
  schedule_expression = "rate(5 minutes)"
}
resource "aws_cloudwatch_event_target" "lambda_target" {
  arn  = aws_lambda_function.s3_file_reader.arn
  rule = aws_cloudwatch_event_rule.lambda_trigger_rule.name
}
resource "aws_lambda_permission" "cloudwatch_lambda_permission" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = "lambda_handler"
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.lambda_trigger_rule.arn
}

#lambda 2
resource "aws_cloudwatch_event_rule" "lambda_2_trigger_rule" {
  name                = "s3_bucket_event_rule"
  description         = "Trigger Lambda when object is written to S3 bucket"
  event_pattern = jsonencode({
    source      = ["aws.s3"],
    detail-type      = [
      "Object Created"
      ],
    detail :{
      bucket:{
        name:[
          aws_s3_bucket.ingestion_bucket.bucket
        ]
      }
    }
    resources   = [aws_s3_bucket.ingestion_bucket.arn],  # "arn:aws:s3:::s3_buck"
  })
}
#lambda 3
resource "aws_cloudwatch_event_rule" "lambda_3_trigger_rule" {
  name                = "s3_bucket_event_rule2"
  description         = "Trigger Lambda when object is written to S3 bucket"
  event_pattern = jsonencode({
    source      = ["aws.s3"],
    detail-type      = [
      "Object Created"
      ],
    detail :{
      bucket:{
        name:[
          aws_s3_bucket.processed_bucket.bucket
        ]
      }
    }
    resources   = [aws_s3_bucket.processed_bucket.arn],  # "arn:aws:s3:::s3_buck"
  })
}

resource "aws_cloudwatch_event_target" "lambda_2_target" {
  rule      = aws_cloudwatch_event_rule.lambda_2_trigger_rule.name
  arn       = aws_lambda_function.s3_processor.arn
}

resource "aws_lambda_permission" "cloudwatch_lambda_2_permission" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = "lambda_handler2" #change to lambda1 name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.lambda_2_trigger_rule.arn
}

resource "aws_cloudwatch_event_target" "lambda_3_target" {
  rule      = aws_cloudwatch_event_rule.lambda_3_trigger_rule.name
  arn       = aws_lambda_function.s3_uploader.arn
}

resource "aws_lambda_permission" "cloudwatch_lambda_3_permission" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = "lambda_handler3" #change to lambda1 name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.lambda_3_trigger_rule.arn
}