docker run -dt                                  \
  -p 9000:9000 -p 9090:9090                     \
  -v PATH:/mnt/data                             \
  -v /etc/default/minio:/etc/config.env         \
  -e "MINIO_CONFIG_ENV_FILE=/etc/config.env"    \
  --name "minio_local"                          \
  --user $(id -u):$(id -g)			\
  quay.io/minio/minio server --console-address ":9090"

